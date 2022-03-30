function solution(new_id) {
  return new_id
    .toLowerCase()
    .replace(/[^\w-_.]/g, "")
    .replace(/\.+/g, ".")
    .replace(/^\.|\.$/, "")
    .replace(/^$/, "a")
    .match(/^.{0,14}[^.]/)[0]
    .replace(/^(.)$/, "$1$1$1")
    .replace(/^(.)(.)$/, "$1$2$2");
}
