; ModuleID = "Programa"
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
  %".8" = fptosi float              0x0 to i32
  ret i32 %".8"
}

define i32 @"main"() 
{
entry:
  %"principal.a" = alloca i32
  %"principal.b" = alloca i32
  %"principal.c" = alloca i32
  %"leiaFlutuante" = call float @"leiaFlutuante"()
  %".2" = fptosi float %"leiaFlutuante" to i32
  store i32 %".2", i32* %"principal.a"
  %".4" = load i32, i32* %"principal.a"
  %"leiaFlutuante.1" = call float @"leiaFlutuante"()
  %".5" = fptosi float %"leiaFlutuante.1" to i32
  store i32 %".5", i32* %"principal.b"
  %".7" = load i32, i32* %"principal.b"
  %".8" = fptosi float              0x0 to i32
  ret i32 %".8"
}
