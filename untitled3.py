
import biomart
from biomart import BiomartServer
server = BiomartServer( "http://www.ensembl.org/biomart" )
db = server.databases['ENSEMBL_MART_ENSEMBL']
hsgene = db.datasets['hsapiens_gene_ensembl']
response = hsgene.search({
  'filters': {
      'ensembl_gene_id': 'ENSG00000074181'
  },
  'attributes': [
      'peptide'
  ]
})
for line in response.iter_lines():
  line = line.decode('utf-8')
  print(line.split("\t"))