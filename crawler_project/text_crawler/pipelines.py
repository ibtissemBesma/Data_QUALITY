# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from openie import StanfordOpenIE
import json

properties = {
    'openie.affinity_probability_cap': 2 / 3,
}
from cleantext.sklearn import CleanTransformer

cleaner = CleanTransformer(no_punct=False, lower=False)
    
class TextCrawlerPipeline:
    def process_item(self, item, spider):
        print(type(item['page_content']))
        text=item['page_content']
        text=text.replace("'",'')
        text=text.replace('|','')
        with StanfordOpenIE(properties=properties) as client:
            triples_corpus=client.annotate(text) 
            
            
            
            print(type(triples_corpus[0]))
            print(triples_corpus)
            
            graph_image = 'graph.png'
            #client.generate_graphviz_graph(text, graph_image)
            #print('Graph generated: %s.' % graph_image)
            
        with open('Data.txt','a', encoding="utf-8") as data_file:
            data_file.write("page URL :"+item["page_url"]+"\n")
            data_file.write("page title :"+item["page_title"][0]+"\n")
            data_file.write("\n ----------------------------------------------------------------------------------------------- \n")
            data_file.write(text)
            data_file.write("\n ----------------------------------------------------------------------------------------------- \n")
            data_file.write("\n ----------------------------------------------------------------------------------------------- \n")
        with open('Triples.txt','a', encoding="utf-8") as triples_file:
            triples_file.write("page URL :"+item["page_url"]+"\n")
            triples_file.write("page title :"+item["page_title"][0]+"\n")
            triples_file.write("\n ----------------------------------------------------------------------------------------------- \n")
            for triple in triples_corpus:
                triples_file.write(json.dumps(triple))
                triples_file.write("\n")
            triples_file.write("\n ----------------------------------------------------------------------------------------------- \n")
            triples_file.write("\n ----------------------------------------------------------------------------------------------- \n")

        return triples_corpus
