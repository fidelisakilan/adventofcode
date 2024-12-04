file = open("input.txt", "r")

reports = []

for levels in file.readlines():
    reports.append([int(i) for i in levels.split()])

safe_reports = 0

def evaluate_reports(report):
    global safe_reports
    last_element = None
    direction = None
    for level in report:
        if last_element is not None:
            new_direction = level - last_element
            if direction is None:
                direction = new_direction
            if not ((0 < abs(new_direction) < 4) and (new_direction * direction) > 0):
                return False
        last_element = level
    return True


for report in reports:
    result = evaluate_reports(report)
    if result:
        safe_reports += 1
print(safe_reports)
