import re

pattern = re.compile(r'^([\d]{4,4})\-[\d]{2,2}\-[\d]{2,2},(.+),(.+),(\d+),(\d+),.*$')
f_csv = None
partidos = 0

def file_csv():
    global f_csv
    global partidos
    with open('/mnt/d/proyectos/platzi/expresiones-regulares/results.csv', mode='r') as f:
        f_csv = [line for line in f]
        for line in f_csv:
            res = re.match(pattern, line)
            if res:
                total = int(res.group(4)) + int(res.group(5))
                if total > 10:
                    print("goles: {}, {}, {} [{}-{}] {}\n".format(total, res.group(1), res.group(2),
                         int(res.group(4)), int(res.group(5)), res.group(3)))
                    partidos += 1
        print('Son {} partidos los que estan impresos\n'.format(int(partidos/2)))

if __name__ == '__main__':

    file_csv()