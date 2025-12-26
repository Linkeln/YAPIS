declare i32 @printf(i8*, ...)
@fmt_int = private unnamed_addr constant [4 x i8] c"%d\0A\00"

define void @get_status(i32* %arg_t, i32* %arg_search_id) {
  %target_row.addr = alloca i32
  store i32 None, i32* %target_row.addr
  %1 = load i32, i32* %target_row.addr
  %2 = load i32, i32* %target_row.addr
  ret void
}
define i32 @main() {
  %my_db.addr = alloca i32
  store i32 None, i32* %my_db.addr
  %user_id.addr = alloca i32
  store i32 101, i32* %user_id.addr
  %res.addr = alloca i32
  store i32 None, i32* %res.addr
  %3 = load i32, i32* %res.addr
  call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @fmt_int, i32 0, i32 0), i32 %3)
  ret i32 0
}