; ModuleID = "ModuloLLVMLITE.bc"
target triple = "unknown-unknown-unknown"
target datalayout = ""

declare float @"escrevaFlutuante"(float %".1") 

declare i32 @"escrevaInteiro"(i32 %".1") 

declare float @"leiaFlutuante"() 

declare i32 @"leiaInteiro"() 

define i32 @"soma"(i32 %"a", i32 %"b") 
{
entry:
  %"a.1" = alloca i32
  store i32 %"a", i32* %"a.1"
  %".5" = load i32, i32* %"a.1"
  %"b.1" = alloca i32
  store i32 %"b", i32* %"b.1"
  %".7" = load i32, i32* %"b.1"
  %"retorno" = alloca i32
  %".8" = load i32, i32* %"a.1"
  ret i32 %".8"
}

define i32 @"main"() 
{
entry:
  %"principal-a" = alloca i32
  %"principal-b" = alloca i32
  %"principal-c" = alloca i32
  %"leiaFlutuante" = call float @"leiaFlutuante"()
  %".2" = fptosi float %"leiaFlutuante" to i32
  store i32 %".2", i32* %"principal-a"
  %".4" = load i32, i32* %"principal-a"
  %"leiaFlutuante.1" = call float @"leiaFlutuante"()
  %".5" = fptosi float %"leiaFlutuante.1" to i32
  store i32 %".5", i32* %"principal-b"
  %".7" = load i32, i32* %"principal-b"
  %".8" = load i32, i32* %"principal-a"
  %".9" = sitofp i32 %".8" to float
  %".10" = load i32, i32* %"principal-b"
  %".11" = sitofp i32 %".10" to float
  %".12" = fptosi float %".9" to i32
  %".13" = fptosi float %".11" to i32
  %".14" = call i32 @"soma"(i32 %".12", i32 %".13")
  %".15" = load i32, i32* %"principal-c"
  %".16" = sitofp i32 %".15" to float
  %".17" = call float @"escrevaFlutuante"(float %".16")
  ret i32 0
}
