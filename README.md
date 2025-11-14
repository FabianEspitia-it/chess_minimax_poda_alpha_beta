## Ajedrez con Minimax y Poda Alfa‑Beta (pygame + python-chess)

Juego de ajedrez con interfaz gráfica en pygame donde juegas con blancas contra una IA que utiliza Minimax con poda Alfa‑Beta. La evaluación combina tablas de valores por casilla (piece-square tables) y varias heurísticas (movilidad, seguridad del rey, estructura de peones, coordinación y control del centro).

### Características
- Interfaz en `pygame` con tablero y piezas renderizadas.
- Resaltado de selección, movimientos legales y capturas.
- IA basada en `python-chess`:
  - Minimax con poda Alfa‑Beta.
  - Ordenamiento de movimientos (capturas MVV‑LVA, promociones, jaques, centralización).
  - Evaluación posicional: material con tablas por casilla, movilidad, seguridad del rey, estructura de peones (peones doblados/pasados), pareja de alfiles, control del centro.
- Configurable: profundidad de búsqueda y tamaño de ventana.

## Requisitos
- Python 3.10 o superior (probado con 3.12).
- Sistema operativo: Windows, macOS o Linux.
- Dependencias Python:
  - `pygame`
  - `python-chess` (y paquete `chess`)

Instálalas con:

```bash
pip install -r requirements.txt
```

## Estructura del proyecto
- `main.py`: bucle principal del juego, entrada del usuario, turnos, renderizado.
- `board.py`: dibujo del tablero, carga de sprites, cálculo de casilla bajo el ratón y resaltados.
- `ai.py`: heurística de evaluación, ordenamiento de movimientos y Minimax con poda Alfa‑Beta.
- `pieces/`: imágenes PNG de las piezas.
- `requirements.txt`: dependencias.

## Cómo ejecutar
1. Crea y activa un entorno virtual (recomendado):
   - Windows (PowerShell):
     ```powershell
     python -m venv .venv
     .\.venv\Scripts\Activate
     ```
   - macOS/Linux (bash):
     ```bash
     python -m venv .venv
     source .venv/bin/activate
     ```
2. Instala dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecuta el juego:
   ```bash
   python main.py
   ```

Si ves un error del tipo “No file 'pieces/white_pawn.png' found in working directory”, asegúrate de ejecutar el comando desde la raíz del proyecto (donde está la carpeta `pieces/`).

## Cómo jugar
- Juegas con blancas (por defecto); la IA juega con negras.
- Clic izquierdo para seleccionar una pieza y clic en una casilla resaltada para mover.
  - Borde dorado: pieza seleccionada.
  - Círculo amarillo: casilla de movimiento legal sin captura.
  - Borde rojo: casilla donde hay captura legal.
- La IA mueve automáticamente tras tu jugada.

## Configuración rápida
- Profundidad de la IA:
  - Por defecto es 3 en `make_ai_move` (archivo `ai.py`).
  - Puedes:
    - Cambiar el valor por defecto en `ai.py`:
      ```python
      def make_ai_move(board, depth=3):  
          ...
      ```
    - O pasar la profundidad desde `main.py`:
      ```python

      make_ai_move(board)

      make_ai_move(board, depth=4)
      ```
  - Nota: profundidad 4 o más puede volverse lenta según tu equipo.

- Tamaño de la ventana/tablero (en `main.py`):
  ```python
  WIDTH, HEIGHT = 640, 640
  SQUARE_SIZE = WIDTH // 8
  ```

- Colores del tablero (en `board.py`):
  ```python
  WHITE = (255, 255, 255)
  BLACK = (105, 146, 62)
  ```

## Detalles del algoritmo
La IA usa Minimax con poda Alfa‑Beta y un ordenamiento de movimientos que prioriza:
- Capturas valiosas (MVV‑LVA).
- Promociones.
- Jaques.
- Movimientos hacia el centro (E4/E5/D4/D5).

La evaluación posicional suma:
\[
\text{score} =
\text{material (tablas por casilla)}
 + 1.5 \cdot \text{movilidad}
 + 2.0 \cdot \text{seguridad del rey}
 + 1.0 \cdot \text{estructura de peones}
 + 1.0 \cdot \text{coordinación de piezas}
 + 0.8 \cdot \text{control del centro}
 \pm \text{bonificación por jaque}
\]

Consideraciones:
- En final (`is_endgame`) se evalúa el rey con una tabla específica de final.
- La seguridad del rey incluye “escudo de peones”.
- Estructura de peones penaliza doblados y premia peones pasados según su avance.
- Coordinación incluye bonificación por pareja de alfiles.
- Control del centro valora presencia y atacantes en casillas centrales/centro extendido.


