---
tags:
  - accuracy
  - hit window
  - OD
  - spinner difficulty
  - presición
  - ventana de golpeo
  - dificultad del spinner
---

# Dificultad general

*Para conocer los valores de OD recomendados, véase: [Criterios de clasificación](/wiki/Ranking_criteria)*

La **dificultad general** u **overall difficulty** (***OD***) define lo difícil que es lograr una alta [precisión](/wiki/Gameplay/Accuracy) en un [beatmap](/wiki/Beatmap). El valor varía de 0 a 10, donde un OD más alto requerirá más exactitud y precisión. Dado que la precisión es importante para ganar [salud](/wiki/Gameplay/Health), la dificultad general también influye en lo difícil que es pasar un beatmap.

## Tiempo

Los valores de OD más altos significan ventanas de tiempo más cortas para completar los [objetos](/wiki/Gameplay/Hit_object), tanto en general como en términos de obtener valores altos de [puntuación](/wiki/Gameplay/Score). El error de golpeo máximo permitido para cada objeto en [osu!](/wiki/Game_mode/osu!) y [osu!mania](/wiki/Game_mode/osu!mania), centrado en el tiempo correcto del objeto, se define en las tablas a continuación.

Ten en cuenta que en la versión estable de osu!, las ventanas de golpeo en osu! y [osu!taiko](/wiki/Game_mode/osu!taiko) pueden ser efectivamente hasta 0.5 ms más cortas a ambos lados de lo que sugieren las fórmulas, y en osu!mania pueden ser hasta 0.5 ms más largas a ambos lados. Esto se debe a que en osu! y osu!taiko, un golpe se considera dentro de una ventana de golpeo si `error de golpeo < redondear(ventana de golpeo)`, mientras que en osu!mania se considera dentro si `error de golpeo  <= redondear(ventana de golpeo)`.[^judgement-rounding-ref]

Por ejemplo, la ventana de golpeo de un Great en osu!taiko en OD 5 es de ±34.5 ms, en lugar de los ±35 ms que da la tabla. En osu!mania, la ventana de golpeo de un MAX es de ±16.5 ms, no de ±16 ms como sugiere la tabla.

Las ventanas de golpeo para los juicios se pueden ver al pasar el cursor sobre la [información del beatmap en el selector de canciones](/wiki/Client/Interface#información-del-mapa), que siempre mostrará los valores correctos.

### osu!

| Puntuación | Ventana de golpeo (ms) |
| --: | :-- |
| 300 | `80 - 6 * OD` |
| 100 | `140 - 8 * OD` |
| 50 | `200 - 10 * OD` |

![](/wiki/shared/ODTable.png "Comparación de las ventanas de golpeo para diferentes combinaciones de OD y modificadores de juego. Para las combinaciones de Half Time y Double Time, los valores de OD mostrados solo son válidos para las ventanas de golpeo de 300 y serían diferentes para las de 100 y 50.")

### osu!taiko

| Puntuación | Ventana de golpeo (ms) |
| --: | :-- |
| Great |  `35 - (35 - 50) * (5 - OD) / 5` si OD < 5, `35 + (20 - 35) * (OD - 5) / 5` si OD > 5, de lo contrario `35` |
| Ok | `80 - (80 - 120) * (5 - OD) / 5` si OD < 5, `80 + (50 - 80) * (OD - 5) / 5` si OD > 5, de lo contrario `80` |
| Miss | `95 - (95 - 135) * (5 - OD) / 5` si OD < 5, `95 + (70 - 95) * (OD - 5) / 5` si OD > 5, de lo contrario `95` |

### osu!mania

| Puntuación | Ventana de golpeo (ms) |
| --: | :-- |
| MAX | `16` |
| 300 | `64 - 3 * OD` |
| 200 | `97 - 3 * OD` |
| 100 | `127 - 3 * OD` |
| 50 | `188 - 3 * OD` |

Si el jugador golpea fuera de la ventana de golpeo de 50, contará como un fallo. En caso de que las ventanas de golpeo de dos objetos se solapen, el segundo objeto será inaccesible hasta que el primer objeto desaparezca debido al [notelock](/wiki/Gameplay/Judgement/Notelock).

## Sliders y spinners

En [osu!](/wiki/Game_mode/osu!), los [sliders](/wiki/Gameplay/Hit_object/Slider) recompensarán con un 300 siempre que se golpee dentro de la ventana de golpeo de 50. Esto a veces se denomina tolerancia del slider y se elimina en [ScoreV2](/wiki/Gameplay/Game_modifier/ScoreV2).

La dificultad general también afecta a los [spinners](/wiki/Gameplay/Hit_object/Spinner), en que deben girarse más para llenar el indicador a tiempo. En [osu!taiko](/wiki/Game_mode/osu!taiko), el denden también necesitará más golpes para ser completado. Los giros por segundo necesarios para completar un spinner se definen mediante la siguiente fórmula:

- OD < 5: `5 - 2 * (5 - OD) / 5`
- OD = 5: `5`
- OD > 5: `5 + 2.5 * (OD - 5) / 5`

## Efectos de mods

Hay cuatro [mods](/wiki/Gameplay/Game_modifier) que alteran la dificultad general cuando se activan:

- [Easy](/wiki/Gameplay/Game_modifier/Easy): Reduce a la mitad el valor del OD.
- [Hard Rock](/wiki/Gameplay/Game_modifier/Hard_Rock): Multiplica el valor del OD por 1.4, hasta un máximo de 10.
- [Double Time](/wiki/Gameplay/Game_modifier/Double_Time): El valor del OD no se ve afectado, pero debido al aumento del 50 % en la velocidad de reproducción, las ventanas de golpeo son un 33 % más cortas.
- [Half Time](/wiki/Gameplay/Game_modifier/Half_Time): El valor del OD no se ve afectado, pero debido a la disminución del 25 % en la velocidad de reproducción, las ventanas de golpeo son un 33 % más largas.

Si bien Half Time y Double Time no cambian el valor del OD, la diferencia de velocidad conduce a un cambio en las ventanas de golpeo. Debido a que la escala es diferente para cada valor de puntuación, DT hace que las ventanas para 100 y 50 sean más estrictas de lo normal en comparación con 300, y HT hace que sean más tolerantes.

## osu!catch

La dificultad general es visible al ver la información del beatmap, pero no afecta el juego.

## Referencias

[^judgement-rounding-ref]: [Mensaje de Discord por spaceman_atlas (6/5/2022) en #osu-wiki en osu!dev](https://discord.com/channels/188630481301012481/218677502141399041/972241866382798889)
