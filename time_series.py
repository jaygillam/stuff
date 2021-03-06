

class TimeSeries(object):
    """For storing x,y data. Data should be in a format of a ordered tuple."""
    def __init__(self, data):
        self.data = data
    
    def get(self, x):
        """This definition finds y for a given x value. :)"""
        for (xi,yi) in self.data:
            if xi == x:
                return yi
        
        raise Exception("Didn't find the value")
    
    def view(self):
        print "data:" self.data


class StepFunctionTimeSeries(TimeSeries):
    """For storing x,y data"""
            
    def get(self, x):
        closest_point = None
        for (xi, yi) in self.data:
            if closest_point is None:
                closest_point = (xi, yi)
            else:
                cx, cy = closest_point
                if abs(xi-x) < abs(cx-x):
                    closest_point = (xi, yi)
        return closest_point[1]

class LinearTimeSeries(TimeSeries):
        """This definition will find cats that like to lie on fences between two values. It will calculate the linear proportion of cat between values/fences"""
    def __init__(self, data):
        TimeSeries.__init__(self, data)
        self.data.sort()
    
    def get(self, x):
        """Get predicted y using linear interpolation of known x,y, given x"""
        # if it's out of range to the left,
        # return the first value
        if x < self.data[0][0]:
            return self.data[0][1]
        # if it's out of range to the right,
        # return the last value
        elif x > self.data[-1][0]:
            return self.data[-1][1]
        # otherwise, it's within the range
        for (n, (xi, yi)) in enumerate(self.data):
            if xi == x:
                return yi
            elif xi > x:
                n1, n2 = n-1, n
                x1, x2 = self.data[n1][0], self.data[n2][0]
                y1, y2 = self.data[n1][1], self.data[n2][1]
                d1, d2 = abs(x-x1), abs(x-x2)
                total_weight = float(d1 + d2)
                w1 = y1 * (total_weight-d1) / total_weight
                w2 = y2 * (total_weight-d2) / total_weight
                return w1 + w2
