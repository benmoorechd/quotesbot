# -*- coding: utf-8 -*-
import scrapy


class ToScrapeCSSSpider(scrapy.Spider):
    name = "www.doralkia.com"
    allowed_domains = ['www.doralkia.com']
    start_urls = ['https://www.doralkia.com/searchnew.aspx']
    rules = [
        Rule(
            LinkExtractor(
                allow=('.*'),
                deny=()
            ),
            callback='parse_item',
            follow=True
        )
    ]
    items = [
        [
            Item(
                CarsForSaleMiamiFlDoralKia1Item,
                None,
                '.col-md-9',
                [
                    Field(
                        'VIN',
                        'div:nth-child(4)::attr(data-vin)',
                        []),
                    Field(
                        'Condition',
                        'div:nth-child(4)::attr(data-vehicletype)',
                        []),
                    Field(
                        'Trim',
                        'div:nth-child(4)::attr(data-trim)',
                        []),
                    Field(
                        'Transmission',
                        'div:nth-child(4)::attr(data-trans)',
                        []),
                    Field(
                        'Stock',
                        'div:nth-child(4)::attr(data-stocknum)',
                        []),
                    Field(
                        'Sale_Price',
                        'div:nth-child(4)::attr(data-price)',
                        []),
                    Field(
                        'MSRP',
                        'div:nth-child(4)::attr(data-msrp)',
                        []),
                    Field(
                        'Bodystyle',
                        'div:nth-child(4)::attr(data-bodystyle)',
                        []),
                    Field(
                        'Certified',
                        'div:nth-child(4)::attr(data-cpo)',
                        []),
                    Field(
                        'Engine',
                        'div:nth-child(4)::attr(data-engine)',
                        []),
                    Field(
                        'Exterior_Color',
                        'div:nth-child(4)::attr(data-extcolor)',
                        []),
                    Field(
                        'Fuel_Type',
                        'div:nth-child(4)::attr(data-fueltype)',
                        []),
                    Field(
                        'Interior_Color',
                        'div:nth-child(4)::attr(data-intcolor)',
                        []),
                    Field(
                        'Make',
                        'div:nth-child(4)::attr(data-make)',
                        []),
                    Field(
                        'Model',
                        'div:nth-child(4)::attr(data-model)',
                        []),
                    Field(
                        'Model_Code',
                        'div:nth-child(4)::attr(data-modelcode)',
                        []),
                    Field(
                        'MPG_City',
                        'div:nth-child(4)::attr(data-mpgcity)',
                        []),
                    Field(
                        'MPG_Highway',
                        'div:nth-child(4)::attr(data-mpghwy)',
                        []),
                    Field(
                        'Full_Title',
                        'div:nth-child(4)::attr(data-name)',
                        []),
                    Field(
                        'Year',
                        'div#srpVehicle-KNDEUCAA0M7050784::attr(data-year)',
                        []),
                    Field(
                        'Image',
                        'div:nth-child(4) > .col-md-12 > .well > .well > .row > div:nth-child(1) > .vehiclePhoto > .img-responsive::attr(data-img)',
                        [],
                        True)])]]
