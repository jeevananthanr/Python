#import common_utils
#import common_utils as cu
#from common_utils import chk_mail_id
from common_utils import *

'''python will search the imported module file in current directory,
C:\Python27\Lib path and in PYTHONPATH environmental var
'''

#res=common_utils.chk_mail_id('jeeva@fmr.com')
#res=cu.chk_mail_id('jeeva@fmr.com')
res=chk_mail_id('jeeva@fmr.com')
print res
