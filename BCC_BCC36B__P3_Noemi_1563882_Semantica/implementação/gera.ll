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
  %"principal-a" = alloca i32
  %"principal-b" = alloca i32
  %"principal-c" = alloca i32
  %"retornoSoma" = add i32 0, 0
  ret i32 %"retornoSoma"
}
