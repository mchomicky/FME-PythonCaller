import fme
import fmeobjects
import re


class FeatureProcessor(object):


    def __init__(self):
        # create RegEx pattern to use for matching on all features
        self.lineMatch = re.compile(r'(Path length[\s\S]*?)?(Design Frequency[\s\S]*?)?(Channel Frequency[\s\S]*?)?(\d{5}[A-Za-z]?(?:_\d)?(?:_MWR)?(?:\sPOP)?(?:_alt\d?)?(?:_old)?:)([\s\S]+?)(?=\d{5}[A-Za-z]?(?:_\d)?(?:_MWR)?(?:\sPOP)?(?:_alt\d?)?(?:_old)?)(\d{5}[A-Za-z]?(?:_\d)?(?:_MWR)?(?:\sPOP)?(?:_alt\d?)?(?:_old)?:)([\s\S]+)')
        
    def input(self, feature):
        # search for match pattern and create match object
        lineMatch = self.lineMatch
        lineString = feature.getAttribute('kml_description')
        mo = lineMatch.search(lineString)
        
        # assign match groups to the corresponding variable
        if mo != None:
            pathLength = mo.group(1)
            designFrequency = mo.group(2)
            channelFrequency = mo.group(3)
            a_name = mo.group(4)
            a_info = mo.group(5)
            b_name = mo.group(6)
            b_info = mo.group(7)
            
            # assign FME attributes if variables not None
            pathLength is not None and feature.setAttribute('Path Length', pathLength.split(':')[1])
            designFrequency is not None and feature.setAttribute('Design Frequency', designFrequency.split(':')[1])
            channelFrequency is not None and feature.setAttribute('Channel Frequency_A', channelFrequency.splitlines()[1])
            channelFrequency is not None and feature.setAttribute('Channel Frequency_B', channelFrequency.splitlines()[2])
            a_name is not None and feature.setAttribute('A_Name', a_name[:-1])
            b_name is not None and feature.setAttribute('B_Name', b_name[:-1])
            
            # loop over a and b info text and split each line into attribute name/value
            if a_info is not None:
                lines = a_info.splitlines()
                for line in lines:
                    if line != '':
                        kv = line.split(':')
                        feature.setAttribute(f'A_{kv[0]}', kv[1])
             
            if b_info is not None:
                lines = b_info.splitlines()
                for line in lines:
                    if line != '':
                        kv = line.split(':')
                        feature.setAttribute(f'B_{kv[0]}', kv[1])
            
        
        self.pyoutput(feature)


    def close(self):
        pass


    def process_group(self):
        pass
