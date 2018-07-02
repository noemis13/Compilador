	.text
	.file	"gera.ll"
	.globl	main                    # -- Begin function main
	.p2align	4, 0x90
	.type	main,@function
main:                                   # @main
	.cfi_startproc
# BB#0:                                 # %entry
	movl	$10, a(%rip)
	xorl	%eax, %eax
	testb	%al, %al
	jne	.LBB0_2
# BB#1:                                 # %entao
	movl	$1, -4(%rsp)
	movl	$10, %eax
	retq
.LBB0_2:                                # %senao
	movl	$10, -4(%rsp)
	movl	$10, %eax
	retq
.Lfunc_end0:
	.size	main, .Lfunc_end0-main
	.cfi_endproc
                                        # -- End function
	.type	a,@object               # @a
	.comm	a,4,4

	.section	".note.GNU-stack","",@progbits
