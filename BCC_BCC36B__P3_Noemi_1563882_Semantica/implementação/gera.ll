; ModuleID = "ModuloLLVMLITE.bc"
target triple = "unknown-unknown-unknown"
target datalayout = ""

declare float @"escrevaFlutuante"(float %".1") 

declare i32 @"escrevaInteiro"(i32 %".1") 

declare float @"leiaFlutuante"() 

declare i32 @"leiaInteiro"() 

define i32 @"main"() 
{
entry:
  %"principal-b" = alloca i32
  %"principal-a" = alloca i32
  store i32 10, i32* %"principal-a"
  %"principal-b.1" = load i32, i32* %"principal-a"
  store i32 %"principal-b.1", i32* %"principal-b"
  ret i32 0
}
