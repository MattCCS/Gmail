#  \/ UNTESTED! \/
for f in files:
    part = email.MIMEBase.MIMEBase('application', "octet-stream")
    part.set_payload( open(f, "rb").read() )
    email.Encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(f))
    msg.attach(part)

for name, data in fileDatas:
    part = email.MIMEBase.MIMEBase('application', "octet-stream")
    part.set_payload(data)
    Encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="%s"' % name)
    msg.attach(part)
