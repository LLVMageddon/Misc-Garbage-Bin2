# 📁 Project File Structure Conventions by Language

This guide outlines standard and idiomatic project structures for commonly used languages. Following these structures improves code clarity, maintenance, and collaboration.

---

## 🛠️ Assembly

```plaintext
project-name/
├── src/
│   ├── main.asm
│   └── utils.asm
├── include/
│   └── macros.inc
├── build/
├── Makefile
└── README.md
```

## 💻 C

```plaintext
project-name/
├── src/
│   ├── main.c
│   └── file_io.c
├── include/
│   └── file_io.h
├── build/
├── tests/
│   └── test_file_io.c
├── Makefile
└── README.md
```

## 🧩 C++
``` plaintext
project-name/
├── src/
│   ├── main.cpp
│   └── logger.cpp
├── include/
│   └── logger.hpp
├── tests/
│   └── test_logger.cpp
├── build/
├── CMakeLists.txt
└── README.md
```

## ☕ Java
``` plaintext
project-name/
├── src/
│   └── main/
│       └── java/
│           └── com/
│               └── example/
│                   └── app/
│                       ├── App.java
│                       └── utils/
│                           └── Helper.java
│   └── test/
│       └── java/
│           └── com/
│               └── example/
│                   └── app/
│                       └── AppTest.java
├── build.gradle / pom.xml
└── README.md
```

## 🐹 Go
```plaintext
project-name/
├── cmd/
│   └── myapp/
│       └── main.go
├── pkg/
│   └── logger/
│       └── logger.go
├── internal/
│   └── utils/
│       └── fileutil.go
├── api/
├── go.mod
├── go.sum
├── README.md
└── tests/
    └── logger_test.go
```

## 🦀 Rust
```plaintext
project-name/
├── src/
│   ├── main.rs
│   ├── lib.rs
│   └── config.rs
├── tests/
│   └── integration_test.rs
├── benches/
├── examples/
├── Cargo.toml
└── README.md
```

## 🌐 JavaScript (Node.js)
```plaintext
project-name/
├── src/
│   ├── index.js
│   ├── services/
│   └── controllers/
├── tests/
│   └── index.test.js
├── public/
├── package.json
├── .eslintrc.json
└── README.md
```

## ✨ TypeScript
```plaintext
project-name/
├── src/
│   ├── index.ts
│   ├── services/
│   └── models/
├── dist/                 # Compiled JS output
├── tests/
│   └── index.test.ts
├── tsconfig.json
├── package.json
├── .eslintrc.json
└── README.md
```

# ✅ Summary Table
| Language   | Source Folder   | Build Config                | Test Folder     | Notes                            |
| ---------- | --------------- | --------------------------- | --------------- | -------------------------------- |
| Assembly   | `src/`          | `Makefile`                  | Manual          | Use `include/` for macros        |
| C          | `src/`          | `Makefile`                  | `tests/`        | Header files in `include/`       |
| C++        | `src/`          | `CMakeLists.txt`            | `tests/`        | Header/source separation         |
| Java       | `src/main/java` | `pom.xml` or `build.gradle` | `src/test/java` | Follows Maven/Gradle standard    |
| Go         | `cmd/`, `pkg/`  | `go.mod`                    | `*_test.go`     | Avoid `vendor/` if using modules |
| Rust       | `src/`          | `Cargo.toml`                | `tests/`        | `lib.rs` if crate                |
| JavaScript | `src/`          | `package.json`              | `tests/`        | Use `public/` for web            |
| TypeScript | `src/`          | `tsconfig.json`             | `tests/`        | Output in `dist/`                |

[Back to README](../README.md)