# ✅ Naming Conventions Guide by Language

A consistent naming convention improves code readability, maintainability, and collaboration across teams. This guide outlines recommended naming practices for these programming languages.

---

## 🛠️ Assembly

- **Project Name**: `lowercase-hyphen` → `boot-loader`
- **Labels**: `UPPERCASE_WITH_UNDERSCORES` → `LOOP_START`
- **Constants**: `UPPERCASE_WITH_UNDERSCORES` → `BUFFER_SIZE`
- **Variables (register aliases or memory)**: `lowercase` → `temp`, `ptr`
- **Functions (macros or labels)**: `lowercase` or `snake_case` → `init_stack`, `main`

---

## 💻 C

- **Project Name**: `lowercase-hyphen` → `http-server`
- **Files/Modules**: `snake_case.c/.h` → `file_io.c`, `utils.h`
- **Functions**: `snake_case` → `read_file()`, `parse_input()`
- **Variables**: `snake_case` → `file_name`, `buffer_size`
- **Constants/Macros**: `UPPERCASE_WITH_UNDERSCORES` → `MAX_BUFFER_SIZE`, `DEFAULT_PORT`
- **Structs/Enums**: `CamelCase` → `User`, `ErrorCode`

---

## 🧩 C++

- **Project Name**: `lowercase-hyphen` → `file-watcher`
- **Files/Modules**: `snake_case.cpp/.h` → `event_loop.cpp`
- **Namespaces**: `lowercase` or `snake_case` → `math`, `string_utils`
- **Classes/Structs**: `CamelCase` → `FileWatcher`, `EventLoop`
- **Functions**: `camelCase` or `snake_case` → `startWatching()`, `read_file()`
- **Variables**: `camelCase` or `snake_case` → `filePath`, `isReady`
- **Constants**: `kCamelCase` or `UPPERCASE_WITH_UNDERSCORES` → `kMaxThreads`, `MAX_SIZE`

---

## ☕ Java

- **Project Name**: `kebab-case` → `spring-framework`
- **Package Names**: `reverse.domain.lowercase` → `com.example.myapp`
- **Classes/Interfaces**: `CamelCase` → `UserService`, `PaymentProcessor`
- **Methods**: `camelCase` → `processPayment()`
- **Variables**: `camelCase` → `totalPrice`, `isVerified`
- **Constants**: `UPPERCASE_WITH_UNDERSCORES` → `MAX_CONNECTIONS`
- **Enums**: `CamelCase` with `UPPERCASE` members → `Status { ACTIVE, INACTIVE }`

---

## 🐹 Go

- **Project Name**: `lowercase` (no hyphens/underscores) → `myapp`, `configloader`
- **Package Names**: `lowercase` → `utils`, `net`
- **Functions**: `CamelCase` for exported, `camelCase` for internal → `PrintLine()`, `readFile()`
- **Variables**: `camelCase` → `userCount`, `fileName`
- **Constants**: `CamelCase` (exported), or `camelCase` → `MaxUsers`, `defaultPort`
- **Structs/Interfaces**: `CamelCase` → `User`, `Logger`
- **Receivers**: short, lowercase → `func (u *User) Save()`

---

## 🦀 Rust

- **Project Name / Crate Name**: `lowercase-hyphen` → `file-io`, `http-client`
- **Modules / Files**: `snake_case` → `parser.rs`, `config.rs`
- **Functions**: `snake_case` → `parse_file()`, `connect_to_server()`
- **Variables**: `snake_case` → `file_path`, `buffer_size`
- **Constants**: `UPPERCASE_WITH_UNDERSCORES` → `MAX_RETRIES`
- **Structs / Enums / Traits**: `CamelCase` → `Config`, `LogLevel`
- **Enum Variants**: `CamelCase` → `Ok`, `NotFound`

---

## 🌐 JavaScript

- **Project Name**: `lowercase-hyphen` → `task-runner`, `web-client`
- **File Names**: `kebab-case.js` or `camelCase.js` → `app-utils.js`, `dataFetcher.js`
- **Variables**: `camelCase` → `userId`, `isLoading`
- **Functions**: `camelCase` → `handleClick()`, `fetchData()`
- **Constants**: `UPPERCASE_WITH_UNDERSCORES` → `MAX_RETRIES`
- **Classes**: `CamelCase` → `HttpClient`, `UserProfile`

---

## ✨ TypeScript

- **Project Name**: `lowercase-hyphen` → `ts-toolkit`, `api-wrapper`
- **Modules / Files**: `kebab-case.ts` or `camelCase.ts` → `auth-service.ts`, `dataParser.ts`
- **Variables**: `camelCase` → `apiToken`, `userEmail`
- **Functions**: `camelCase` → `getUserInfo()`, `validateInput()`
- **Constants**: `UPPERCASE_WITH_UNDERSCORES` → `DEFAULT_TIMEOUT`
- **Types/Interfaces**: `PascalCase` → `User`, `RequestPayload`
- **Enums**: `PascalCase` and members in `CamelCase` → `Role { Admin, Guest }`

---

## ✅ Summary Table

| Element         | C / C++       | Java           | Go            | Rust          | JS / TS       | Assembly       |
|------------------|----------------|----------------|----------------|----------------|----------------|-----------------|
| Project Name     | `lowercase-hyphen` | `kebab-case`   | `lowercase`   | `lowercase-hyphen` | `kebab-case`   | `lowercase-hyphen` |
| File/Module      | `snake_case`  | `lowerCamelCase` | `lowercase`   | `snake_case`  | `camelCase` / `kebab-case` | `snake_case` |
| Function Name    | `snake_case`  | `camelCase`    | `CamelCase` (exported) | `snake_case` | `camelCase`    | `snake_case` / `lowercase` |
| Variable Name    | `snake_case`  | `camelCase`    | `camelCase`   | `snake_case`  | `camelCase`    | `lowercase` |
| Constant         | `UPPERCASE`   | `UPPERCASE`    | `CamelCase`   | `UPPERCASE`   | `UPPERCASE`    | `UPPERCASE` |
| Class/Struct     | `CamelCase`   | `CamelCase`    | `CamelCase`   | `CamelCase`   | `CamelCase`    | (N/A) |
| Enum / Type      | `CamelCase`   | `CamelCase` + `UPPERCASE` variants | `CamelCase` | `CamelCase`   | `PascalCase`   | (N/A) |

[Back to README](../README.md)