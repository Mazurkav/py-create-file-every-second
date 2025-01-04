import time


def create_file() -> None:
    while True:
        current_time = time.localtime()
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S.%f", current_time)
        file_name = {
            f"app-{current_time.hour}_{current_time.min}_{current_time.sec}.log"
        }
        with open(file_name, "w") as f:
            f.write(timestamp)
        print(f"{timestamp} {file_name}")
        time.sleep(1)


if __name__ == "__main__":
    create_file()
