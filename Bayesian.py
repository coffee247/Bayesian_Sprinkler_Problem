import json
import re

class bayesian_sprinkler():
    config = dict()
    boolvals = {}
    def __init__(self):
        """ Create a new bayesian sprinnkler object """
        with open('probabilities.json') as json_data:
            self.config = json.load(json_data)  # load database connection parameters from config.json
        self.boolvals = {0: "FFF", 1: "FFT", 2: "FTF", 3: "FTT", 4: "TFF", 5: "TFT", 6: "TTF", 7: "TTT"}

    def makeMask(self, sprinkler, rain, wetgrass):
        nodelist = [sprinkler, rain, wetgrass]
        mask = 0
        removed = 0
        for i, value in enumerate(nodelist): # iterate through the input values
            if (value == None):  # first check the the value for the node is None
                if (i == 0):
                    removed+=(4)  # append column binary position to list of columns removed
                elif (i == 1):
                    removed+=(2)  # append column binary position to list of columns removed
                else:
                    removed+=(1)
            elif (value == True):
                if (i == 0): #  Sprinkler
                    mask+=4 # add column binary position to mask value
                elif(i == 1): # Rain
                    mask+=2 # add column binary position to mask value
                else:  # Wetgrass
                    mask+=1  # add column binary position to mask value
        return mask, removed

    def pIsWet(self, mask, removed):
        wetgrass = (self.config.get('p_wetgrass'))[0]
        returnval = 0
        if (removed %2 != 0):  # if removed is odd (wetgrass value is None)
            return("Wetgrass must have a value (cannot be None)")
        elif (removed == 6): # Both rain and sprinkler removed
            ''' All but wetgrass column removed 
            (Only the terminal node remains in Asynchronous Durected Graph) Probability always sums to 1.0")'''
            return (1.0)
        elif (removed == 4): # sprinkler removed
            if (mask == 2): # and mask is True only for rain (user input was None, True, False)
                for key in wetgrass:
                    if ((key == 'FTF') or (key == 'TTF')):  # match None True False
                        returnval = round(returnval + wetgrass.get(key), 3)
                return returnval
            if (mask == 3): # mask is True for rain and wetgrass (user input was None, True, True)
                for key in wetgrass:
                    if ((key == 'FTT') or (key == 'TTT')):
                        returnval = round(returnval + wetgrass.get(key), 3)
                return returnval
            if (mask == 1): # mask is True only for wetgrass (user input was None, False, True)
                for key in wetgrass:
                    if ((key == 'FFT') or (key == 'TFT')):
                        returnval = round(returnval + wetgrass.get(key), 3)
                return returnval
            if (mask == 0):
                for key in wetgrass:
                    if ((key == 'FFF') or (key == 'TFF')):
                        returnval = round(returnval + wetgrass.get(key), 3)
                return returnval
        elif (removed == 2): # rain removed
            if (mask == 5): # mask is True only for sprinkler and wetgrass (user input was True, None, True)
                for key in wetgrass:
                    if ((key == 'TFT') or (key == 'TTT')):
                        returnval = round(returnval + wetgrass.get(key), 3)
                return returnval
            if (mask == 4): # mask is True only for sprinkler (user input was True, None, False)
                for key in wetgrass:
                    if ((key == 'TFF') or (key == 'TTF')):
                        returnval = round(returnval + wetgrass.get(key), 3)
                return returnval
            if (mask == 1): # mask is True only for wetgrass (user input was False, None, True)
                for key in wetgrass:
                    if ((key == 'FFT') or (key == 'FTT')):
                        returnval = round(returnval + wetgrass.get(key), 3)
                return returnval
            if (mask == 0):
                for key in wetgrass:
                    if ((key == 'FFF') or (key == 'FTF')):
                        returnval = round(returnval + wetgrass.get(key), 3)
                return returnval
        else:
            return((self.config.get('p_wetgrass')[0]).get(self.boolvals.get(mask)))

def main():
    mysprinkler = bayesian_sprinkler()

    mask, removed = mysprinkler.makeMask(True, None, False)
    print("\n{}".format(mysprinkler.pIsWet(mask, removed)))
    print("Produced by:\n\t{}, but ignoring element in place {}"
          .format(mysprinkler.boolvals.get(mask), removed))

if __name__ == '__main__':
    main();