# Echoes of Lumina

![Echoes of Lumina Banner](assets/banner.png)

**Echoes of Lumina** is a captivating 2D puzzle-adventure game set in a vibrant, bioluminescent world. Players step into the shoes of Lumina, a guardian spirit with the ability to manipulate light and shadows. Traverse through mesmerizing landscapes, solve intricate puzzles, and uncover the mysteries of a forgotten civilization in this enchanting journey.

---

## Table of Contents

- [Echoes of Lumina](#echoes-of-lumina)
  - [Table of Contents](#table-of-contents)
  - [Game Overview](#game-overview)
  - [Features](#features)
  - [Screenshots](#screenshots)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
    - [Running the Game](#running-the-game)
  - [Gameplay](#gameplay)
    - [Controls](#controls)
    - [Game Mechanics](#game-mechanics)
  - [Assets](#assets)
    - [Character: Lumina](#character-lumina)
    - [Light Effect](#light-effect)
    - [Environment](#environment)
  - [Contributing](#contributing)
  - [Credits](#credits)
  - [License](#license)
  - [Contact](#contact)

---

## Game Overview

**Echoes of Lumina** invites players to explore a beautifully hand-drawn 2D world illuminated by bioluminescent flora and fauna. As Lumina, navigate through lush forests, crystalline caves, and ethereal temples by mastering the art of light manipulation. Use light and shadows to reveal hidden paths, activate ancient mechanisms, and solve challenging puzzles. Immerse yourself in a story-rich environment where every corner holds a secret waiting to be discovered.

---

## Features

- **Dynamic Light Manipulation:**
  - Move and control light sources to cast shadows, reveal hidden objects, and create platforms.
  - Utilize shadows for strategic advantages like hiding from enemies or unlocking secret areas.

- **Bioluminescent Environments:**
  - Explore diverse and vibrant landscapes, including lush forests, crystalline caves, and ethereal temples.
  - Experience day-night cycles that influence puzzle mechanics and enemy behavior.

- **Engaging Storyline:**
  - Unravel the history of Lumina’s world through environmental storytelling, ancient texts, and interactions with other spirits.
  - Meet diverse characters, each with their own backstories and quests.

- **Challenging Puzzles:**
  - **Light Reflection:** Use mirrors and prisms to direct beams of light.
  - **Shadow Puzzles:** Align shadows to form symbols or pathways.
  - **Environmental Interaction:** Manipulate elements like water, wind, and flora to progress.

- **Artistic Visuals and Sound:**
  - Hand-drawn 2D art with vibrant colors and fluid animations.
  - An ambient soundtrack that adapts to the player's actions and the environment.

---

## Screenshots

![Forest Level](assets/screenshots/forest_level.png)
*Explore the lush, bioluminescent forests.*

![Puzzle Mechanic](assets/screenshots/puzzle_mechanic.png)
*Manipulate light and shadows to solve intricate puzzles.*

![Lumina in Action](assets/screenshots/lumina_action.png)
*Lumina using her powers to navigate through the environment.*

---

## Getting Started

### Prerequisites

- **Python 3.7 or higher**: Ensure you have Python installed. Download it from [python.org](https://www.python.org/downloads/).
- **Pygame Library**: Install Pygame using pip.

```bash
pip install pygame
```

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/echoes_of_lumina.git
   ```

2. **Navigate to the Project Directory:**

   ```bash
   cd echoes_of_lumina
   ```

3. **Install Dependencies:**

   Ensure all required Python libraries are installed. For this project, Pygame is essential.

   ```bash
   pip install -r requirements.txt
   ```

### Running the Game

Execute the main Python script to start the game.

```bash
python main.py
```

---

## Gameplay

### Controls

- **Movement:**
  - `W` / `Up Arrow`: Move Up
  - `A` / `Left Arrow`: Move Left
  - `S` / `Down Arrow`: Move Down
  - `D` / `Right Arrow`: Move Right

- **Interact:** `E` key
- **Pause Menu:** `Esc` key

### Game Mechanics

- **Light Manipulation:**
  - Move Lumina to control the position of light sources.
  - Cast shadows to create pathways, solve puzzles, and evade enemies.

- **Puzzle Solving:**
  - Use mirrors and prisms to redirect light beams.
  - Align shadows to form specific shapes or symbols.
  - Interact with environmental elements like water and wind to progress.

- **Exploration:**
  - Traverse through various bioluminescent environments.
  - Discover hidden areas and uncover the lore of Lumina’s world.

---

## Assets

### Character: Lumina (`assets/lumina.png`)

- **Description:** Lumina is the protagonist, a guardian spirit with the ability to manipulate light and shadows.
- **Design:** Hand-drawn with a semi-transparent, glowing effect to emphasize her ethereal nature.
- **Resolution:** 128x128 pixels.
- **Animation:** Includes frames for idle and walking animations.

![Lumina](assets/lumina.png)

### Light Effect (`assets/light.png`)

- **Description:** Represents the dynamic light emanating from Lumina, used for illumination and shadow casting.
- **Design:** A radial gradient with a bright center fading into transparency, enhanced with subtle sparkles for realism.
- **Resolution:** 512x512 pixels.
- **Usage:** Blended using `pygame.BLEND_RGBA_ADD` for realistic lighting effects.

![Light Effect](assets/light.png)

### Environment

- **Backgrounds:** Hand-drawn 2D environments including forests, caves, and temples.
- **Obstacles:** Designed with shadows in mind to interact seamlessly with the light mechanics.
- **Interactive Elements:** Mirrors, prisms, crystals, and other objects that respond to light manipulation.

---

## Contributing

Contributions are welcome! Whether you're a developer, artist, or just someone who wants to help, your input is valuable.

1. **Fork the Repository**
2. **Create a Feature Branch**

   ```bash
   git checkout -b feature/YourFeature
   ```

3. **Commit Your Changes**

   ```bash
   git commit -m "Add Your Feature"
   ```

4. **Push to the Branch**

   ```bash
   git push origin feature/YourFeature
   ```

5. **Open a Pull Request**

Please ensure your contributions adhere to the project's coding standards and guidelines.

---

## Credits

- **Development:** [Your Name](https://github.com/yourusername)
- **Art & Design:** [Artist's Name](https://github.com/artistusername) *(if applicable)*
- **Soundtrack:** [Composer's Name](https://github.com/composerusername) *(if applicable)*
- **Special Thanks:**
  - [OpenGameArt](https://opengameart.org/) for various assets.
  - [Pygame Community](https://www.pygame.org/) for the invaluable library and support.

---

## License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute this project, but please respect the original creators and contributors.

---

## Contact

For any inquiries, feedback, or support, please reach out to:

- **Email:** agiaftermath@gmail.com
- **Twitter:** [@yourtwitterhandle](https://twitter.com/yourtwitterhandle)

We’d love to hear your thoughts and suggestions!

---

**Embark on a luminous journey with Lumina and uncover the secrets that lie in the shadows. Welcome to the world of Echoes of Lumina!**
