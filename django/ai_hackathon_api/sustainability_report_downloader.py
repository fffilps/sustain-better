# Import libraries
import os
import requests
from bs4 import BeautifulSoup
from django.core.files.base import ContentFile
from ai_hackathon_api.models import Company, CompanyReport

class SustainabilityReportDownloader:
    # URL from which pdfs to be downloaded
    base_url = "https://www.responsibilityreports.com"
    company_base_url = base_url + "/Companies?search="
    search_link = '/Company/'
    companies_dir = "/companies"
    pdfs_dir = "./media" + companies_dir
    url = None
    company_name = None
    pdfs_path = None

    def __init__(self, company_name):
        self.company_name = company_name
        self.url = self.company_base_url + company_name
        clean_company_name = company_name.replace(' ', '_')
        self.pdfs_company_dir = self.pdfs_dir + "/" +  clean_company_name
        self.mkdir(self.pdfs_company_dir)
    
    def mkdir(self, dir_path):  
        # Check whether the specified path exists or not
        does_exist = os.path.exists(dir_path)
        if not does_exist:
            # Create a new directory because it does not exist
            os.makedirs(dir_path)

    def parse_company_link(self, link):
        link_href = link.get('href', [])
        if (self.search_link in link_href):
            return link_href
        return None
    
    def save_report_pdf(self, pdf_contents, pdf_name, report_year):
        pdf_filename = self.pdfs_company_dir + "/" + self.company_name + "_" + pdf_name
        pdf_filename = pdf_filename.replace(' ', '_')
        try:
            print("saving" + pdf_filename)
            company_obj = Company.objects.get(name=self.company_name)

            content_file_path = pdf_filename.replace('media/', '')
            print("content_file_path" + content_file_path)
            pdf_file = ContentFile(pdf_contents)
            pdf_file.name = content_file_path
            
            pdf = open(pdf_filename, 'wb')
            pdf.write(pdf_contents)
            pdf.close()

            tmp_report = CompanyReport(
                # Save the fields with the values from Visit
                company = company_obj,
                pdf = pdf_file,
                pdf_name = pdf_filename,
                year = report_year
            )
            tmp_report.save()

        except Exception as e:
            print("save_report_pdf: Exception caught ")
            print(e)

        print("pdf_filename saved " + pdf_filename)

    def download_pdf(self, link_href, pdf_name, report_year):
        try:
            company_obj = Company.objects.get(name=self.company_name)
            
            if not CompanyReport.objects.filter(company=company_obj, year=report_year).exists():
                pdf_url = self.base_url + link_href
                # Get response object for link
                response = requests.get(pdf_url)
                # Write content in pdf file
                self.save_report_pdf(response.content, pdf_name, report_year)
            else:
                print("already exists")
        except Exception as e:
            print("download_pdf: Exception caught ")
            print(e)

    def get_links_from_page(self, url):
        response = requests.get(url)
        # Parse text obtained
        soup = BeautifulSoup(response.text, 'html.parser')
        # Find all hyperlinks present on webpage
        links = soup.find_all('a')

        return links

    def call_company_api(self):
        links = self.get_links_from_page(self.url)
        # From all links check for pdf link and
        # if present download file
        company_href = None
        for link in links:
            company_href = self.parse_company_link(link)
            if company_href:
                break
        
        company_url = self.base_url + company_href
        company_links = self.get_links_from_page(company_url)

        for company_link in company_links:
            link_href = company_link.get('href', [])
            if ('.pdf' in link_href): 
                parts = link_href.split('/')
                pdf_name = parts[-1]
                year_parts = pdf_name.split("_")[-1]
                report_year = os.path.splitext(year_parts)[0]
                self.download_pdf(link_href, pdf_name, report_year)
            