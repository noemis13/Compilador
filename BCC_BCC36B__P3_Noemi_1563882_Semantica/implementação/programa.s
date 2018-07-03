	.text
	.file	"programa.ll"
	.globl	soma                    # -- Begin function soma
	.p2align	4, 0x90
	.type	soma,@function
soma:                                   # @soma
	.cfi_startproc
# BB#0:                                 # %entry
	movl	%edi, -4(%rsp)
	cvtsi2ssl	%edi, %xmm0
	cvttss2si	%xmm0, %eax
	retq
.Lfunc_end0:
	.size	soma, .Lfunc_end0-soma
	.cfi_endproc
                                        # -- End function
	.globl	main                    # -- Begin function main
	.p2align	4, 0x90
	.type	main,@function
main:                                   # @main
	.cfi_startproc
# BB#0:                                 # %entry
	subq	$24, %rsp
.Lcfi0:
	.cfi_def_cfa_offset 32
	callq	leiaFlutuante
	cvttss2si	%xmm0, %eax
	movl	%eax, 12(%rsp)
	callq	leiaFlutuante
	cvttss2si	%xmm0, %eax
	movl	%eax, 20(%rsp)
	cvtsi2ssl	12(%rsp), %xmm0
	cvttss2si	%xmm0, %edi
	callq	soma
	movl	%eax, 16(%rsp)
	xorps	%xmm0, %xmm0
	cvtsi2ssl	%eax, %xmm0
	callq	escrevaFlutuante
	xorl	%eax, %eax
	addq	$24, %rsp
	retq
.Lfunc_end1:
	.size	main, .Lfunc_end1-main
	.cfi_endproc
                                        # -- End function

	.section	".note.GNU-stack","",@progbits
