import params.params as par

def convertDistance(units, value):
# Table for 2 multipliers specified by given units in units
  multipliers = []
# Getting those multipliers by their keys from defined dictionary
  multipliers.append(par.distanceUnitsDict[units[0]])
  multipliers.append(par.distanceUnitsDict[units[1]])
  result = value * multipliers[1] / multipliers[0]

  return result


def convertMass(units, value):
    # Table for 2 multipliers specified by given units in units
    multipliers = []
    # Getting those multipliers by their keys from defined dictionary
    multipliers.append(par.massUnitsDict[units[0]])
    multipliers.append(par.massUnitsDict[units[1]])
    result = value * multipliers[1] / multipliers[0]

    return result