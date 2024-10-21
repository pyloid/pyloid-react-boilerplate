# Pyloid-React

Pyloid-React-Boilerplate is a template for projects combining a React frontend with a Python backend. Here, we'll explain in detail the project setup, development, and build process.

### Prerequisites

- [Prerequisites](https://docs.pyloid.com/getting-started/prerequisites)

## 1. Project Initialization

Before starting the project, you need to install all necessary dependencies.

```bash
npm run init
```

This command performs the following tasks:

1. Install npm packages
2. Create a Python virtual environment (venv-pyloid)
3. Install Python dependencies (based on requirements.txt)

The appropriate script is executed depending on the operating system.

## 2. Running the Development Server

During development, you can run both frontend and backend servers simultaneously with the following command:

```bash
npm run dev
```

This command performs the following tasks:

1. Run the React frontend development server using Vite
2. Run the Python backend server (src-pyloid/main.py)

The concurrently package is used to run both processes in parallel.

## 3. Building the Project

To build the project for production deployment, use the following command:

```bash
npm run build
```

This command performs the following tasks:

1. TypeScript compilation (tsc -b)
2. Frontend build using Vite
3. Package the Python backend into an executable using PyInstaller

### Backend Packaging with PyInstaller

PyInstaller is a tool that converts Python applications into standalone executables. Pyloid Boilerplate uses different spec files for each operating system:

- Windows: `build-windows.spec`
- Linux: `build-linux.spec`
- MacOS: `build-macos.spec`

These spec files specify which files to include and what options to use for PyInstaller.

### How PyInstaller Works

1. Dependency Analysis: PyInstaller analyzes the Python script and its dependencies.
2. File Collection: It collects all necessary Python modules, libraries, and data files.
3. Binary Generation: It packages the collected files into a single directory or a single executable file.

### Custom Build Process

You can modify the build process to meet your project's specific requirements:

1. Modify the scripts section in `package.json`
2. Modify PyInstaller spec files (e.g., `build-windows.spec`, `build-linux.spec`, `build-macos.spec`)
3. Write additional build scripts if necessary

### Important Notes

- Cross-platform Builds: You need to perform the build for each platform on the respective operating system.
- Environment Variables: You may need to set environment variables appropriately depending on the production environment.

This guide should help you understand the process of initializing, developing, and building a project using the Pylon Boilerplate. Backend packaging with PyInstaller simplifies deployment and facilitates dependency management.
