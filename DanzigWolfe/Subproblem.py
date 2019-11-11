from ortools.sat.python import cp_model
from collections import namedtuple
from collections import defaultdict


def SubProblem(jobs_data):
    models = []
    num_machines = 1 + max(task[0] for job in jobs_data for task in job)
    all_machines = range(num_machines)
    for machine in all_machines:
        models.append(cp_model.CpModel())

    horizon = sum(task[1] for job in jobs_data for task in job)

    task_type = namedtuple('task_type', 'start_end_interval')

    assigned_task_type = namedtuple('assigned_task_type', 'start_job_idx_duration')

    # Create job interval and add to the corresponding list
    all_tasks = {}
    machine_to_intervals = defaultdict(list)

    for job_idx, job in enumerate(jobs_data):
        for task_idx, task in enumerate(job):
            machine_idx = task[0]
            model = models[machine_idx]
            duration = task[1]
            suffix = '_%i_%i' % (job_idx, task_idx)

            start_var = model.NewIntVar(0, horizon, 'start' + suffix)
            end_var = model.NewIntVar(0, horizon, 'end' + suffix)
            interval_var = model.NewIntervalVar(start_var, duration, end_var, 'interval' + suffix)

            all_tasks[job_idx, task_idx] = task_type(start=start_var, end=end_var, interval=interval_var)

            machine_to_intervals[machine_idx].append(interval_var)

    # Disjunctive constraint
    for machine_idx in all_machines:
        models[machine_idx].AddNoOverlap(machine_to_intervals[machine_idx])







