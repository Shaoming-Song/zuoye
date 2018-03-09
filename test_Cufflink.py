from Cufflinks import Cufflinks
from stepbase import Configure,Schedule

import os

Configure.setRefDir(os.path.join(os.path.expanduser('~'),'songshaoming/ref'))
Configure.setGenome('hg19')

cflk = Cufflinks(bamInput=['./minidata/accepted_hits.bam'],
				gtfInput=['./minidata/genome.gtf'],
				outputDir=['./']
				)

Schedule.run()
