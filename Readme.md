# AI Strings

```python
from dotenv import load_dotenv

from aistrings import AiStrings

load_dotenv()

astr = AiStrings(provider_name="openai", model_name="gpt-3.5-turbo-0125")
response = astr.summarize(
    "Mars is the fourth planet from the Sun. The surface of Mars is orange-red because it is covered in iron(III) oxide dust, giving it the nickname 'the Red Planet'.[21][22]"
    " Mars is among the brightest objects in Earth's sky, and its high-contrast albedo features have made it a common subject for telescope viewing. "
    "It is classified as a terrestrial planet and is the second smallest of the Solar System's planets with a diameter of 6,779 km (4,212 mi). "
    "In terms of orbital motion, a Martian solar day (sol) is equal to 24.5 hours, and a Martian solar year is equal to 1.88 Earth years (687 Earth days). "
    "Mars has two natural satellites that are small and irregular in shape: Phobos and Deimos. "
)
print(response)

```

Output:

```
Mars is the fourth planet from the Sun, known as the Red Planet due to its orange-red surface covered in iron(III) oxide dust. 
It is a terrestrial planet with a diameter of 6,779 km and has a solar day of 24.5 hours and a solar year of 1.88 Earth years. 
Mars has two small, irregular-shaped natural satellites: Phobos and Deimos.
```

Keep track of the cost:

```python
# get total cost only
print("Total Cost", astr.cumulative_cost)
# get full history + total cost 
astr.log_history()
```

Output:

```
Total Cost: 0.0002235

History
----------------------
  Action: summarize
  Input: Mars is the fourth planet from the Sun. The surface of Mars is orange-red because it is covered in iron(III) oxide dust, giving it the nickname 'the Red Planet'.[21][22] Mars is among the brightest objects in Earth's sky, and its high-contrast albedo features have made it a common subject for telescope viewing. It is classified as a terrestrial planet and is the second smallest of the Solar System's planets with a diameter of 6,779 km (4,212 mi). In terms of orbital motion, a Martian solar day (sol) is equal to 24.5 hours, and a Martian solar year is equal to 1.88 Earth years (687 Earth days). Mars has two natural satellites that are small and irregular in shape: Phobos and Deimos. 
  Output: Mars is the fourth planet from the Sun, known as the Red Planet due to its orange-red surface covered in iron(III) oxide dust. It is a terrestrial planet with a diameter of 6,779 km and has a solar day of 24.5 hours and a solar year of 1.88 Earth years. Mars has two small, irregular-shaped natural satellites: Phobos and Deimos.
  Cost: 0.0002235
  Time: 2024-05-14 13:57:53.797679

Total Cost: 0.0002235
----------------------
```


