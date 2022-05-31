import fme
import fmeobjects


class FeatureProcessor(object):


    def __init__(self):
        pass

    def input(self, feature):
        kmlData = feature.getAttribute('kml_description')
        lines = kmlData.splitlines()
        pairs = []
        
        for line in lines:
            if line != '':
                pair = line.split(':')
                pairs.append([pair[0], pair[1]])
        
        
        for pair in pairs:
            feature.setAttribute(pair[0], pair[1])

        self.pyoutput(feature)
    def close(self):

        pass

    def process_group(self):

        pass
