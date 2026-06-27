print("Hello Mars")
try:
    with open("mission_computer_main.log", "r", encoding="utf-8") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("로그 파일을 찾을 수 없습니다.")

except UnicodeDecodeError:
    print("파일 인코딩을 읽을 수 없습니다.")

except PermissionError:
    print("파일에 접근할 권한이 없습니다.")

except OSError as error:
    print("파일 처리 중 오류가 발생했습니다:", error)