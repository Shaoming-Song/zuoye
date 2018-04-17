from ..core import Flow,Report,Configure,Schedule
from ..core import SC3_DE,SCDE_diff

class DiffExp(Flow):
	def __init__(self,
				 algorithm = 'SC3',
				 matrixdata = None,
				 c3matrix_file= None,
				 matrix_format = 'ORIGIN',
				 sc3ann = "",
				 resultDir='./result'):
	super(DiffExp, self).__init__(resultDir = resultDir,
								  refDir = None,
								  genome = None,
								  threads = None)
	self._setParam('algorithm', algorithm)
        #set Monocle parameters
    self._setParam('matrixdata',matrixdata)
    self._setParam('sc3matrix_file',sc3matrix_file)
	self._setParam('matrix_format',matrix_format)
	self._setParam('sc3ann',sc3ann)

    def _call(self,*args):
        # args[0]._getObj('FastqDump').getOutput('fastqOutput')
        pass

    def _build(self,):
        algorithm = self._getParam('algorithm')
        if algorithm=='SCDE':
        	matrixdata = self._getParam('matrixdata')
        	SCDE_result = SCDE_diff(matrixdata = matrixdata,
        						outputpath = None)

        	rp = Report()
        	rp.add('SCDE results',[SCDE_result])

        	self._setObj('SCDE_result',SCDE_result)

        elif algorithm=='sc3':
        	sc3matrix_file = self._getParam('sc3matrix_file')
            matrix_format = self._getParam('matrix_format')
            sc3ann = self._getParam('sc3ann')
            sce = SingleCellExperiment(matrix_file=sc3matrix_file,
                                       ann_file=sc3ann, 
                                       matrix_format='ORIGIN')
            sc3_de = SC3_DE()(sce)
            rp = Report()
            rp.add('SingleCellExperiment Results',[sce])
            rp.add('SC3 differential expression results',[sc3_de])

            self._setObj('sce',sce)
            self._setObj('sc3_de',sc3_de)

        else:
        	print('This algorithm is unavailable!') 

        def _copy(self,):
        	algorithm = self._getParam('algorithm')
        	if algorithm == 'sc3':
        		self._linkRecursive(self._getObj('sc3_de').getOutput('sc3Output_De_genes.table'),
                                self.getFinalRsPath('sc3Output_Result'))
        	elif algorithm == 'SCDE':
        		pass
        	else:
        		print('This algorithm is unavailable!') 
        		
