import random
import re
import string

__author__ = 'michal'


def random_string(length=6, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(length))


FLOAT_WITH_COEFFICIENT_REGEX = re.compile(
    r'(?P<fl>\d+([.,]\d+)?)(?P<coeff>[KkMm])?'
)
THOUSAND_COEFFICIENT_REGEX = re.compile('[Kk]')
MILLION_COEFFICIENT_REGEX = re.compile('[Mm]')


def parse_float_with_coefficient(float_str):
    match = FLOAT_WITH_COEFFICIENT_REGEX.match(float_str)
    if not match:
        raise ValueError
    strength = float(match.group('fl'))
    coeff_string = match.group('coeff')
    if coeff_string:
        coeff = THOUSAND_COEFFICIENT_REGEX.match(coeff_string) and 1000 or \
            1000000
        return coeff * strength
    return strength
