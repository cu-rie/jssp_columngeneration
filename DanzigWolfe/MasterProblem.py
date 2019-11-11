from ortools.sat.python import cp_model


# def MasterProblem(object):
#     def __init__(self, num_machines, num_jobs, initial, vars):
#         model = cp_model.CpModel()
#
#
#     def add_constraint(self, ):
#         pass
#
#     def solve(self):
#         pass
class Masterproblem(object):
    def __init__(self, num_jobs, num_machines):
        self.num_jobs = num_jobs
        self.num_machines = num_machines

    def solve(self, y_lists):
        model = cp_model.CpModel()

        # objective

        c_max = model.NewIntVar(lb=0, ub=9999, name='c_max')
        expressions = []
        for i in range(len(y_lists)):
            y = model.NewIntVar(lb=0, ub=0, name="y_{}".format(i))
            expressions.append(y)
        for i in range(len(y_lists)):
            job_time = y_lists[i]
            coeff = []
            for j in job_time:
                coeff.append(j)

            scalprod = cp_model.LinearExpr.ScalProd(expressions, coeff)
            model.AddMaxEquality(c_max, scalprod)

        model.Minimize(c_max)


if __name__ == "__main__":
    y_lists = [[0, 1, 2, 3],
               [2, 3, 1, 4]]
    master = Masterproblem(num_jobs=4, num_machines=5)
    master.solve(y_lists)
