#!/bin/bash

# Usage: ./init-go-project.sh myproject github.com/yourusername/myproject

set -e

PROJECT_NAME=$1
MODULE_NAME=$2

if [ -z "$PROJECT_NAME" ] || [ -z "$MODULE_NAME" ]; then
    echo "Usage: $0 <project-name> <module-path>"
    echo "Example: $0 inventory-service github.com/yourname/inventory-service"
    exit 1
fi

echo "Creating project structure for '$PROJECT_NAME' with module '$MODULE_NAME'..."

mkdir -p $PROJECT_NAME/{cmd/$PROJECT_NAME,internal/db,pkg/user,api,configs,scripts,tests}

cd $PROJECT_NAME

# Init go module
go mod init "$MODULE_NAME"

# Create main.go entrypoint
cat <<EOF > main.go
package main

import "fmt"

func main() {
    fmt.Println("Starting $PROJECT_NAME...")
}
EOF

# Create cmd entrypoint
cat <<EOF > cmd/$PROJECT_NAME/main.go
package main

import "fmt"

func main() {
    fmt.Println("$PROJECT_NAME service launched.")
}
EOF


# Create test entrypoint
cat <<EOF > tests/test_test.go
package tests

import (
    "testing"
)

// Add is a simple example function to be tested.
func Add(a, b int) int {
    return a + b
}

func TestAdd(t *testing.T) {
    cases := []struct {
        name     string
        a, b     int
        expected int
    }{
        {"1 + 1", 1, 1, 2},
        {"0 + 0", 0, 0, 0},
        {"-1 + 1", -1, 1, 0},
        }

    for _, c := range cases {
        t.Run(c.name, func(t *testing.T) {
            result := Add(c.a, c.b)
            if result != c.expected {
                t.Errorf("Add(%d, %d) = %d; want %d", c.a, c.b, result, c.expected)
            }
        })
    }
}
EOF




# Create Makefile
cat <<EOF > Makefile
# Project variables
APP_NAME := $PROJECT_NAME
MAIN_FILE := main.go

.PHONY: all
all: build

.PHONY: build
build:
$(echo -e '\t')go build -o bin/\$(APP_NAME) \$(MAIN_FILE)

.PHONY: run
run: build
$(echo -e '\t')./bin/\$(APP_NAME)

.PHONY: test
test:
$(echo -e '\t')go test ./tests/... -v

.PHONY: fmt
fmt:
$(echo -e '\t')go fmt ./...

.PHONY: vet
vet:
$(echo -e '\t')go vet ./...

.PHONY: clean
clean:
$(echo -e '\t')rm -rf bin
EOF


# Touch other files
touch internal/db/db.go
touch pkg/user/service.go
touch README.md

# Create .gitignore
cat <<EOF > .gitignore
# Binaries
*.exe
*.exe~
*.dll
*.so
*.dylib
*.test

# Output
/bin/
/build/
/dist/

# Dependency directories
vendor/

# IDE/editor files
.idea/
.vscode/
*.swp

# OS files
.DS_Store
EOF

echo "✅ Project '$PROJECT_NAME' initialized successfully."
