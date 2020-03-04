input = [
    "time, type, revenue, gross revenue",
    "2018-09-12 08:17, contract",
    "2018-09-12 09:20,  transient,$22",
    "2018-09-12 08:01,contract",
    "2018-09-12 09:21,   contract",
    "2018-09-12 11:18,  transient, $22",
    "2018-09-12 12:11,discount,$17,$22",
    "2018-09-12 13:05,contract",
    "2018-09-12 13:48,contract",
    "2018-09-12 13:55,discount,$10,$32",
    "2018-09-12 14:08, transient, $5.5",
    "2018-09-12 14:29, discount, $30, $32",
    "2018-09-12 10:02, contract",
    "2018-09-12 09:40,  contract",
    "2018-09-12 10:25, discount,$2.75, $5.5",
    "2018-09-12 10:42,  discount, $4.5, $9.5",
    "2018-09-12 09:21,discount, $17,$22",
    "2018-09-12 11:08, transient, ($9.5)",
    "2018-09-12 12:22, transient, $9.0",
    "2018-09-12 12:31,   transient,   $15",
    "2018-09-12 09:21,discount,($17),null",
    "2018-09-12 09:21,transient,22",
    "2018-09-12 12:58,   transient,   $15",
    "2018-09-12 11:08,transient,$32",
    "2018-09-12 14:50,discount, $10, $32",
    "2018-09-12 15:30,   transient,   $9.5",
    "2018-09-12 15:42,   contract",
    "2018-09-12 15:56,   transient,   $32",
    "2018-09-12 15:58,   transient, $9.5",
    "2018-09-12 09:25, contract",
    "2018-09-12 10:08, transient, $9.0",
    "2018-09-12 10:21, discount, $2.75, $5.5",
    "2018-09-12 11:55,transient, 15.0",
    "2018-09-12 13:03, discount, $12, 25",
    "2018-09-12 13:03,contract",
    "2018-09-12 12:30,  discount,20,  $25.0",
    "2018-09-12 12:31,discount,10 ,25",
    "2018-09-12 12:48,discount,$2.5,  $25",
    "2018-09-12 14:08,transient,$22",
    "2018-09-12 13:55, discount, $12, $22",
]

def topFiveTransient(input):
    transients = [i for i in input if (i.split(",")[1]).strip() == "transient"]
    if len(transients) <= 1:
        return transients

    def func(x):
        if x.split(",")[2].strip()[0] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            return float(x.split(",")[2].strip())
        elif x.split(",")[2].strip()[0] == "(":
            return float(x.split(",")[2].strip()[2:][:-1])
        else:
            return float(x.split(",")[2].strip()[1:])
    sorted_transient = sorted(transients, key=func)
    return sorted_transient[::-1][:5]


test = topFiveTransient(input)
print(test)
