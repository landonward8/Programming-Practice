'''
ResidencyMatch.py

This algorithm operates by reading an input file of the form

[residents | hospitals] preference 1, preference 2, preference 3, preference 4, ...

Any whitespace occurring in the input files is stripped off.

Usage:

    python ResidencyMatch.py [residents preference file] [hospitals preference file]

[Landon Ward]

'''

import sys
import csv

class ResidencyMatch:

    # behaves like a constructor
    def __init__(self):
        '''
        Think of
        
            unmatchedHospitals
            residentsMappings
            hospitalsMappings
            matches
            
        as being instance data for your class.
        
        Whenever you want to refer to instance data, you must
        prepend it with 'self.<instance data>'
        '''
        
        # list of unmatched hospitals
        self.unmatchedHospitals = [ ]

        # list of unmatched residents
        self.unmatchedResidents = [ ]
        
        # dictionaries representing preferences mappings
        
        self.residentsMappings = { }
        self.hospitalsMappings = { }
        
        # dictionary of matches where mapping is resident:hospital
        self.matches = { }
        
        # read in the preference files
        
        '''
        This constructs a dictionary mapping a resident to a list of hospitals in order of preference
        '''
        
        prefsReader = csv.reader(open (sys.argv[1],'r'), delimiter = ',')
        for row in prefsReader:
            resident = row[0].strip()

             # all hospitals are initially unmatched
            self.unmatchedResidents.append(resident)

            # maps a resident to a list of preferences
            self.residentsMappings[resident] = [x.strip() for x in row[1:]]
            
            # initially have each resident as unmatched
            self.matches[resident] = None
        
        '''
        This constructs a dictionary mapping a hospital to a list of residents in order of preference
        '''
        
        prefsReader = csv.reader(open (sys.argv[2],'r'), delimiter = ',')
        for row in prefsReader:
            
            hospital = row[0].strip()
            
            # all hospitals are initially unmatched
            self.unmatchedHospitals.append(hospital)
            
            # maps a resident to a list of preferences
            self.hospitalsMappings[hospital] = [x.strip() for x in row[1:]] 
    
            
    # print out the stable match
    def reportMatches(self):
        print(self.matches)
            
    # follow the chart described in the lab to find the stable match
    def runMatch(self):
        '''
        It is suggested you use the debugger or similar output statements
        to determine what the contents of the data structures are
        '''  
        # as long as there are unmatched residentsk
        while self.unmatchedResidents:
            for resident in self.unmatchedResidents:
                #  get the list of prefferedHospitals for each resident
                preferredHospitals = self.residentsMappings[resident]
                for hospital in preferredHospitals:
                    # if the hospital is not matched yet, match the resident with the first hospital
                    if hospital in self.unmatchedHospitals: 
                        self.matches[resident] = hospital
                        self.unmatchedResidents.remove(resident)
                        self.unmatchedHospitals.remove(hospital)
                        break
                    else:
                        current_match = [resident for resident, hospital in self.matches.items() if hospital == hospital][0]
                        hospital_preferences = self.hospitalsMappings[hospital]
                        
                        if hospital_preferences.index(resident) < hospital_preferences.index(current_match):
                            self.matches[current_match] = None
                            self.unmatchedResidents.append(current_match)
                            self.matches[resident] = hospital
                            self.unmatchedResidents.remove(resident)
                            break
        
            

           # hospitalPreferences = self.hospitalsMappings[hospital]


if __name__ == "__main__":
   
    # some error checking
    if len(sys.argv) != 3:
        print('ERROR: Usage\n python ResidencyMatch.py [residents preferences] [hospitals preferences]')
        quit()

    # create an instance of ResidencyMatch 
    match = ResidencyMatch()

    # now call the runMatch() function
    match.runMatch()
    
    # report the matches
    match.reportMatches()



