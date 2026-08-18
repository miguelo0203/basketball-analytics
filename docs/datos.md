# Datos, Procedencia y Esquemas Relacionales

## 1. Cobertura del Almacén de Datos

El almacén relacional DuckDB (`data/03_validated/basketball_analytics.duckdb`) consolida dos décadas de competiciones internacionales de selecciones masculinas absolutas (2005–2024).

```
+----------------------------------------------------------------------------------------------------+
| ENTIDAD / DIMENSIÓN          | VALOR AUDITADO EN REPOSITORIO                                       |
+----------------------------------------------------------------------------------------------------+
| **Torneos Oficiales**        | 18 Torneos (EuroBasket, Copa del Mundo FIBA, Juegos Olímpicos)      |
| **Periodo Temporal**         | 2005 a 2024 (cobertura histórica completa)                          |
| **Partidos Totales**         | 1.145 Partidos internacionales oficiales                            |
| **Observaciones Equipo**     | 2.290 Filas en `fact_team_game`                                     |
| **Actuaciones de Jugador**   | 27.353 Registros individuales en `fact_player_game`                  |
| **Campañas de Jugador**      | 4.350 Campañas torneo-jugador (3.767 cualificadas con >= 40 min)    |
| **Jugadores Canónicos**      | 2.124 Jugadores únicos normalizados con resolución de entidades    |
| **Esquema Relacional**       | 12 Tablas relacionales normalizadas en DuckDB                       |
+----------------------------------------------------------------------------------------------------+
```

---

## 2. Esquema Relacional en DuckDB

```text
dim_tournament (tournament_id, name, year, tournament_type, host_country, ...)
dim_team (team_id, team_code, team_name, confederation, ...)
dim_player (player_id, canonical_name, birth_year, height_cm, position_nominal, ...)
dim_coach (coach_id, coach_name, nationality, ...)

fact_game (game_id, tournament_id, game_date, team_a_id, team_b_id, score_a, score_b, pace, ...)
fact_team_game (team_game_id, game_id, team_id, is_home, points, fgm, fga, fg3m, fg3a, ftm, fta, ...)
fact_player_game (player_game_id, game_id, player_id, minutes, points, reb, ast, stl, blk, tov, ...)

mart_player_roles (player_id, tournament_id, cluster_id, role_name, pca_x, pca_y, ...)
mart_tactical_video (possession_id, game_id, team_id, action_type, drop_depth, contest_speed, ...)
```

---

## 3. Calidad de Datos y Reconciliación Matemática

Cada acta bruta ingresada en el lago se valida contra tres reglas deterministas:
1. **Regla de Minutos**: La suma de los minutos de todos los jugadores de un equipo debe igualar exactamente $200.0$ minutos reglamentarios (o $225.0 / 250.0$ en prórrogas).
2. **Regla de Marcador**: La suma de puntos anotados por los jugadores de un equipo debe coincidir con el marcador oficial registrado.
3. **Regla de Posesiones**: Las posesiones estimadas deben guardar coherencia bilateral entre ambos equipos según la fórmula canónica de Dean Oliver.

---

## 4. Resolución de Entidades
Se diseñó un motor determinista de resolución de entidades para unificar variaciones tipográficas, acentos y transliteraciones (ej. "Pau Gasol", "Gasol Sáez, Pau", "P. Gasol") asignando un único `player_id` canónico para garantizar la continuidad longitudinal.

---

## 5. Procedencia y Licencias
- Los datos proceden de estadísticas oficiales públicas de FIBA y el Comité Olímpico Internacional.
- No se incluye ningún dato privado, sensible ni protegido bajo licencias comerciales de pago.
