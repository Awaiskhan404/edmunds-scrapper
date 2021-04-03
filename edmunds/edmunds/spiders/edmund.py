#kira
import scrapy
import pandas as pd 
class car(scrapy.Spider):
    http_user='someuser'#imp shit if you skip u get dns error
    http_pass='somepass'
    name='edmund'#name of spider
    start_urls=[
        
        'https://www.edmunds.com/car-incentives/'
        
        ]
    def parse(self, response):   
        for cars in response.css('a.text-primary-darker::attr(href)'):
            url = response.urljoin(cars.extract())
            yield scrapy.Request(url, callback = self.parse_dir_contents)#going to next page

    def parse_dir_contents(self, response):
        for links in response.css('a.incentives-link.text-primary-darker.d-flex.flex-column.h-100::attr(href)'):
            url=response.urljoin(links.extract())
            yield scrapy.Request(url, callback = self.final_parse)#going to next page
    def final_parse(self,response):
        self.Student=[]
        self.military=[]
        self.First_Responder=[]
        self.Customer_Bonus=[]
        self.Loyalty=[]
        self.Conquest=[]
        self.Mobility=[]
        self.Loyalty_Lender_Bonus_Cash=[]
        self.Student_College_Grad_Lender_Bonus=[]
        self.Conquest_for_Retail=[]
        self.Mobility_for_Retail=[]
        self.Clean_Fuel_Rebate_for_Retail_or_Lease=[]
        self.Military_for_Lease=[]
        self.Customer_Bonus_Cash_for_Retail=[]
        self.Lender_Bonus_for_Standard_APR=[]
        self.Student_College_Grad_for_Lease=[]
        self.First_Responder_for_Lease=[]
        self.Military_for_Retail=[]
        self.First_Responder_for_Retail=[]
        self.Limited_Term_Bonus_Cash=[]

        self.offers=response.css('li.unordered-list-item')
        self.cash_offers=self.offers.css('span::text').getall()
        for self.offer in self.cash_offers:
            #our AI LOL ;-)
            if 'Student/College Grad for Retail or Lease' in self.offer:
                self.Student.append(self.offer)
            elif 'Military for Retail or Lease' in self.offer:
                self.military.append(self.offer)
            elif 'First Responder for Retail or Lease' in self.offer:
                self.First_Responder.append(self.offer)
            elif 'Lease Bonus Cash' in self.offer:
                self.Customer_Bonus.append(self.offer)
            elif 'Loyalty for Retail or Lease' in self.offer:
                self.Loyalty.append(self.offer)
            elif 'Mobility for Retail' in self.offer:
                self.Mobility.append(self.offer)
            elif 'Conquest for Retail or Lease' in self.offer:
                self.Conquest.append(self.offer)
            elif 'Loyalty Lender Bonus Cash' in self.offer:
                self.Loyalty_Lender_Bonus_Cash.append(self.offer)
            elif 'Student/College Grad Lender Bonus' in self.offer:
                self.Student_College_Grad_Lender_Bonus.append(self.offer)
            elif 'Conquest for Retail' in self.offer:
                self.Conquest_for_Retail.append(self.offer)
            elif 'Mobility for Retail' in self.offer:
                self.Mobility_for_Retail.append(self.offer)
            elif 'Clean Fuel Rebate for Retail or Lease' in self.offer:
                self.Clean_Fuel_Rebate_for_Retail_or_Lease.append(self.offer)
            elif 'Military for Lease' in self.offer:
                self.Military_for_Lease.append(self.offer)
            elif 'Customer Bonus Cash for Retail' in self.offer:
                self.Customer_Bonus_Cash_for_Retail.append(self.offer)
            elif 'Lender Bonus for Standard APR' in self.offer:
                self.Lender_Bonus_for_Standard_APR.append(self.offer)
            elif 'Student/College Grad for Lease' in self.offer:
                self.Student_College_Grad_for_Lease.append(self.offer)
            elif 'First Responder for Lease' in self.offer:
                self.First_Responder_for_Lease.append(self.offer)
            elif 'Military for Retail' in self.offer:
                self.Military_for_Retail.append(self.offer)
            elif 'First Responder for Retail' in self.offer:
                self.First_Responder_for_Retail.append(self.offer)
            elif 'Limited Term Bonus Cash' in self.offer:
                self.Limited_Term_Bonus_Cash.append(self.offer)
            else:
                pass
        self.trim_value=response.css('option::text').getall()
        for self.trim_name in self.trim_value:
            self.trim_data=self.trim_name
            yield{
                'Name':response.css('h1.heading-2.mb-1_5::text').extract_first().split()[1],
                'Model':response.css('h1.heading-2.mb-1_5::text').get(),
                'Trim':self.trim_data,
                'Student/College Grad for Retail or Lease':self.Student,
                'Military for Retail or Lease':self.military,
                'First Responder for Retail or Lease':self.First_Responder,
                'Lease Bonus Cash':self.Customer_Bonus,
                'Loyalty for Retail or Lease':self.Loyalty,
                'Conquest for Retail or Lease':self.Conquest,
                'Mobility for Retail':self.Mobility,
                'Loyalty Lender Bonus Cash':self.Loyalty_Lender_Bonus_Cash,
                'Student/College Grad Lender Bonus':self.Student_College_Grad_Lender_Bonus,
                'Conquest for Retail':self.Conquest_for_Retail,
                'Mobility for Retail':self.Mobility_for_Retail,
                'Clean Fuel Rebate for Retail or Lease':self.Clean_Fuel_Rebate_for_Retail_or_Lease,
                'Military for Lease':self.Military_for_Lease,
                'Customer Bonus Cash for Retail':self.Customer_Bonus_Cash_for_Retail,
                'Lender Bonus for Standard APR':self.Lender_Bonus_for_Standard_APR,
                'Student/College Grad for Lease':self.Student_College_Grad_for_Lease,
                'First Responder for Lease':self.First_Responder_for_Lease,
                'Military for Retail':self.Military_for_Retail,
                'First Responder for Retail':self.First_Responder_for_Retail,
                'Limited Term Bonus Cash':self.Limited_Term_Bonus_Cash,
            }#writing the data