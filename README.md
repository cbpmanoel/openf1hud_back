# OpenF1HUD

## Overview

The idea of this project is to build a telemetry application for F1 games, composed of the following components:

* HUD Module: the real-time interface for the driver.

* Dashboard Module: the post-race analysis and configuration workspace. It includes tools for reviewing telemetry data, editing HUD layouts, and managing application settings.

* (Stretch) PitWall Module: a real-time, in-race telemetry analysis environment for teams or engineers.

The project architecture consists of a backend service that listens for UDP telemetry data from the game, stores it in a database for the dashboard, and simultaneously broadcasts live data to the frontend.
