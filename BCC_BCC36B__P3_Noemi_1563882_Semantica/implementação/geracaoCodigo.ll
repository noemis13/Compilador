; ModuleID = "ModuloLLVMLITE"
target triple = "unknown-unknown-unknown"
target datalayout = ""

@"global-a" = external global i32
define i32 @"principal"() 
{
entry:
  %"principal-b" = alloca i32
  store i32 10, i32* @"global-a"
  %".3" = load i32, i32* @"global-a"
}
