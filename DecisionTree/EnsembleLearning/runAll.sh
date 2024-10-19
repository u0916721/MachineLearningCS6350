echo "Choose an option:"
echo "1) Run AdaBoost"
echo "2) Run Bagged Trees"
echo "3) Run Random Forest"
echo "4) Run all of the above"
read -p "Enter a choice (1-4): " gangsta
case $gangsta in
    1)
        python3 ada_boost.py
        ;;
    2)
        python3 bagged_trees.py run_bagged_trees
        ;;
    3)
        python3 bagged_trees.py runRandomForest
        ;;
    4)
        echo "RUNNING ALL"
        python3 ada_boost.py
        python3 bagged_trees.py run_bagged_trees
        python3 bagged_trees.py runRandomForest
        ;;
esac
