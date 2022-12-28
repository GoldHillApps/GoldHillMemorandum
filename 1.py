import ybc_ui
t=ybc_ui.input()
o=ybc_ui.picker_button('',['检查','不检查'])
if o=='检查':
    ybc_ui.message(t)
    t2=ybc_ui.input()
    o2=ybc_ui.picker_button('',['完毕'])
    if o2=='完毕':
        f=open('文字.txt','a')
        f.write(t2+'\n')
        f.close()
else:
    f=open('文字.txt','a')
    f.write(t+'\n')
    f.close()
