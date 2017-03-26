class StreamParser(object):

    def __init__(self, stream):
        self.stream = stream
        self.stats = stream.stats()
        self.values = stream.values
        self.min = self.stats['stats']['min']
        self.max = self.stats['stats']['max']
        self.mean = self.stats['stats']['avg']
        self.stddev = self.stats['stats']['stddev']
        self.count = self.stats['stats']['count']

    def return_rounded_unicode(self, value):
        return str(round(float(value), 2))

    def get_mean(self):
        return self.return_rounded_unicode(self.mean)

    def get_min(self):
        return self.return_rounded_unicode(self.min)

    def get_max(self):
        return self.return_rounded_unicode(self.max)

    def get_count(self):
        return int(self.count)


class FlowStream(StreamParser):

    def __init__(self, stream):
        super(FlowStream, self).__init__(stream)
        self.total = float(self.mean) * float(self.count)

    def get_total(self):
        return self.return_rounded_unicode(self.total)
