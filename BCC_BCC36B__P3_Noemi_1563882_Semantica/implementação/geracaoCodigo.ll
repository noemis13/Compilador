; ModuleID = "ModuloLLVMLITE"
target triple = "unknown-unknown-unknown"
target datalayout = ""

@"global-a" = external global i32
define i32 @"main"() 
{
entry:
  %"principal-b" = alloca i32
  store i32 10, i32* @"global-a"
  store i32 10, i32* %"principal-b"
}
