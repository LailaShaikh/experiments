import luigi


class BaseTask(luigi.Task):
    def run(self):
        print "Running dep tasks"
        self.output().open('w').close()
        #return

    def output(self):
        return luigi.LocalTarget('dep.out')
        

class MainTask(luigi.Task):
    x = luigi.IntParameter()
    y = luigi.IntParameter()
    add_action = luigi.BoolParameter()

    def requires(self):
        return BaseTask()

    def run(self):
        if self.add_action:
            self.res = self.x + self.y
        else:
            self.res = self.x - self.y
        with self.output().open('w') as fobj:
            fobj.write("Result is %s" % self.res)
        
    def output(self):
        return luigi.LocalTarget('result.out')


if __name__ == '__main__':
    luigi.run()
