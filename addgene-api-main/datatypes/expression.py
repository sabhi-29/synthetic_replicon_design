from typing import Annotated, Literal

from pydantic import AfterValidator


ExpressionIn = Literal[
  "bacterial",
  "mammalian",
  "insect",
  "plant",
  "worm",
  "yeast",
  "insect,",
  "mamm…",
  "mammalian,",
  "y…",
  'mammalia…',
  'w…',
  'plant,',
  'yeast…'
]

ExpressionOut = Literal[
  "Bacterial Expression",
  "Mammalian Expression",
  "Insect Expression",
  "Plant Expression",
  "Worm Expression",
  "Yeast Expression",
]

EXPRESSION_MAP: dict[ExpressionIn, ExpressionOut] = {
  "bacterial": "Bacterial Expression",
  "mammalian": "Mammalian Expression",
  "insect": "Insect Expression",
  "plant": "Plant Expression",
  "worm": "Worm Expression",
  "yeast": "Yeast Expression",
  "insect,": "Insect Expression",
  "mamm…": "Mammalian Expression",
  "y…": "Yeast Expression",
  "mammalian,": "Mammalian Expression",
  'mammalia…': "Mammalian Expression",
  'w…': "Worm Expression",
  'yeast…': "Yeast Expression",
  'plant,': "Plant Expression"
}

Expression = Annotated[ExpressionIn, AfterValidator(EXPRESSION_MAP.get)]
