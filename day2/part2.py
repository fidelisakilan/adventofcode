file = open("input.txt", "r")

reports = []

for levels in file.readlines():
    reports.append([int(i) for i in levels.split()])

safe_reports = 0
# 559 601

def evaluate_report(report):
    setpos = set({1, 2, 3})
    setneg = set({-1, -2, -3})
    for i in range(0, len(report) - 1):
        diff = report[i + 1] - report[i]
        setpos.add(diff)
        setneg.add(diff)

    return len(setpos) == 3 or len(setneg) == 3


for report in reports:
    if evaluate_report(report):
        safe_reports += 1
    else:
        for i in range(len(report)):
            if evaluate_report(report[:i] + report[i + 1 :]):
                safe_reports += 1
                break
print(safe_reports)

# report = [1, 2, 3, 4, 5]
# print(report)
# for i in range(0, len(report) - 1):
#     print(report[:i] + report[i + 1 :], report[: i + 1] + report[i + 2 :])
