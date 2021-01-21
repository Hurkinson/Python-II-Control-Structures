import toolbox

fn = r"C:\Users\Hurkinson\.spyder-py3\Python II Control Structures\countingcats.py"
with open(fn, 'r', encoding='utf8') as f:
    s = f.read()

mDc = toolbox.get_counts(s)

with open('output.txt', 'w', encoding='utf8') as f:
    for k in mDc.keys():
        f.write(k)

f =  open('output.txt', 'w', encoding='utf8')
try:
    for k in mDc.keys():
        f.write(k)
finally:
    f.close()

        

