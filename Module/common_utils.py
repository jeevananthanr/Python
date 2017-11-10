def chk_mail_id(mail_id):
    status=''
    if len(mail_id)>0:
        if mail_id.endswith('@fmr.com',2):
            status= "Valid Mail id"
        else:
            status= "Invalid Email id"
    else:
        status= "insufficient argument"

    return (status)

'''result=chk_mail_id('jeevananthanr@fmr.com')
if result is not None:
    print result'''
