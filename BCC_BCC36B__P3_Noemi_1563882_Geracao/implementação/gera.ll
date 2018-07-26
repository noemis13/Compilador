; ModuleID = "ModuloLLVMLITE.bc"
target triple = "unknown-unknown-unknown"
target datalayout = ""

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
  %"retorno.1" = alloca i32
  %".9" = load i32, i32* %"a.1"
  %"retornoSoma" = add i32 %".9", %".8"
  store i32 %"retornoSoma", i32* %"a.1"
  ret i32 %"retornoSoma"
}

define i32 @"main"() 
{
entry:
  %"principal-a" = alloca i32
  %"principal-b" = alloca i32
  %"principal-c" = alloca i32
  %"leiaInteiro" = call i32 @"leiaInteiro"()
  store i32 %"leiaInteiro", i32* %"principal-a"
  %"leiaInteiro.1" = call i32 @"leiaInteiro"()
  store i32 %"leiaInteiro.1", i32* %"principal-b"
  %".4" = load i32, i32* %"principal-a"
  %".5" = sitofp i32 %".4" to float
  %".6" = load i32, i32* %"principal-b"
  %".7" = sitofp i32 %".6" to float
  %".8" = fptosi float %".5" to i32
  %".9" = fptosi float %".7" to i32
  %".10" = call i32 @"soma"(i32 %".8", i32 %".9")
  %".11" = load i32, i32* %"principal-a"
  %".12" = call i32 @"escrevaInteiro"(i32 %".11")
  ret i32 0
}

declare i32 @"escrevaInteiro"(i32 %".1") 
