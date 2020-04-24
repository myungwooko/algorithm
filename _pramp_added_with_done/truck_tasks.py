#
# Complete the 'is_blocked' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts following parameters:
#  1. STRING_ARRAY required_tasks
#  2. STRING_ARRAY task_from
#  3. STRING_ARRAY task_to
# required_task

def is_blocked(required_tasks, task_from, task_to):
    # Write your code here
    res = []
    for i in range(len(task_from)):
        if task_from[i] in required_tasks:
            from_val = task_from[i]
            to_val = task_to[i]
            from_idx_at_required = required_tasks.index(from_val)
            #이거 처리는 일단 간단한 거였는데
            if to_val in required_tasks:
                to_idx_at_required = required_tasks.index(to_val)
                if from_idx_at_required < to_idx_at_required:
                    res.append(task_from[i])
                else:
                    return True
            else:
                res.append(task_from[i])
    res.sort()
    required_tasks.sort()
    if required_tasks == res:
        return False
    for i, task in enumerate(task_to):
        if task in required_tasks and task not in res:
            res.append(task)
    res.sort()
    required_tasks.sort()

    if required_tasks == res:
        return False

    return True


re = ['get gas', 'drive', 'exit']
fro = ['get gas', 'drive', 'load materials', 'exit']
tp = ['drive', 'exit','exit','load materials']
test = is_blocked(re, fro, tp)
print(test)